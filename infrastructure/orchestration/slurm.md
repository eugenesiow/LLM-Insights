# SLURM

SLURM, originally an acronym for Simple Linux Utility for Resource Management (though this acronym is now deprecated), is an open-source workload manager specifically designed for Linux clusters of all sizes. It is known for its scalability, fault tolerance, and comprehensive feature set and powers a significant portion of the world's largest supercomputers.

## Architecture

SLURM's architecture is designed around a central management daemon, `slurmctld`, which runs on a management node (often with a fail-over backup for high availability) and orchestrates all scheduling activities. This daemon monitors resources and pending jobs, makes allocation decisions, and manages the job lifecycle. On each compute node, a `slurmd` daemon runs, acting as a local agent that executes tasks assigned by `slurmctld`, monitors local resources, and reports status back. Optionally, `slurmdbd` (SLURM Database Daemon) can be deployed to interface with a database (typically MySQL/MariaDB) for persistent storage of job accounting records, enforcement of resource limits across multiple clusters, and historical data analysis. A `slurmrestd` daemon provides a REST API for programmatic interaction with SLURM.

## Scheduling

### `sched/builtin`

**Algorithm:** The `sched/builtin` plugin implements a straightforward scheduling algorithm based on strict job priority order. Within each priority level and within each partition, it generally operates on a First-In, First-Out (FIFO) basis. It attempts to schedule jobs sequentially, starting from the highest priority pending job.

**Operational Logic:** The scheduler iterates through pending jobs in strict priority order within a given partition. It evaluates the highest priority job to see if sufficient resources are currently available for it to start. If the highest priority job cannot run (e.g., due to insufficient nodes, memory, or GRES), the `sched/builtin` logic, in its default configuration, will not consider any lower-priority jobs within that same partition during that scheduling pass. This strict adherence to priority prevents lower-priority jobs from potentially taking resources that the higher-priority job might need shortly.

**Pros:**

* **Simplicity:** The logic is relatively easy to understand, configure, and predict.
* **Predictability:** Users can generally expect jobs to start in priority order, assuming resources become available sequentially. The highest priority job that fits available resources is guaranteed the next allocation.

**Cons:**

* **Low Utilization:** This scheduler can lead to significant resource wastage due to "Head-of-Line Blocking." If a high-priority job requires a large number of resources that are not currently free, it blocks the scheduler from considering any subsequent, lower-priority jobs in that partition, even if those jobs are small and could run immediately on the currently idle resources.
* **Reduced Throughput:** As a consequence of potential low utilization, the overall rate of job completion (throughput) may be lower compared to more sophisticated scheduling algorithms like backfill.

**Configuration:** To use this scheduler, administrators set `SchedulerType=sched/builtin` in the `slurm.conf` file. Parameters like `default_queue_depth`, `sched_interval`, and `partition_job_depth` still influence when and how many jobs are considered in each scheduling cycle.

### `sched/backfill`

**Algorithm:** The `sched/backfill` scheduler is the most commonly used scheduler in modern SLURM deployments. It enhances the priority-based scheduling of `sched/builtin` with a sophisticated backfill mechanism. Backfilling involves simulating future resource availability to identify opportunities where lower-priority jobs can be started "early" without delaying the anticipated start times of higher-priority jobs.

**Operational Logic:** The process typically involves these steps:

1.  **Priority Scheduling:** Similar to `builtin`, the scheduler first attempts to schedule jobs in strict priority order.
2.  **Reservation:** It identifies the highest-priority pending jobs that cannot currently start. Based on the estimated completion times of currently running jobs and the resource requirements of these high-priority pending jobs, the scheduler calculates their expected future start times and conceptually reserves the necessary resources for them.
3.  **Backfill Candidate Search:** The scheduler then iterates through the queue of lower-priority jobs. For each lower-priority job, it checks if it can be allocated resources and if its estimated runtime is short enough for it to complete before the earliest reserved start time of any higher-priority job whose resources it would overlap with.
4.  **Backfill Execution:** If a lower-priority job meets these criteria, it is "backfilled" – started immediately, even though higher-priority jobs are still pending.

**Pros:**

* **Improved Cluster Utilization:** Backfilling significantly reduces idle node time by proactively filling resource gaps with suitable smaller or shorter-duration jobs that would otherwise have to wait.
* **Increased Throughput:** By keeping resources busier, the overall number of jobs completed over a given period generally increases.
* **Better Diagnostics:** The simulation process allows the backfill scheduler to often provide more specific reasons why a job is pending (e.g., `ReqNodeNotAvail`, `Resources`, or even indicating resources are reserved for a specific higher-priority job).

**Cons:**

* **Increased Scheduler Overhead:** The resource simulation required for backfill calculations is computationally more intensive than the simple FIFO check performed by `sched/builtin`. This can increase the load on the `slurmctld` daemon, especially on very large clusters or clusters with high job submission rates.
* **Less Intuitive Scheduling Order:** Since jobs can start out of strict priority order, the scheduling behavior can sometimes appear less predictable or confusing to end-users.
* **Sensitivity to Job Estimates:** The effectiveness of backfill scheduling is highly dependent on having reasonably accurate estimates of job runtimes. If jobs specify excessively long wall times, the scheduler will reserve resources unnecessarily far into the future, hindering backfill opportunities. Conversely, jobs that terminate prematurely due to underestimating runtime waste the allocated resources and the scheduling effort. While SLURM often uses partition or QoS time limits as fallbacks, accurate user-provided estimates (`#SBATCH -t 5`) are beneficial. SLURM's accounting tracks actual usage, but scheduling decisions rely on requested limits.

**Configuration:** This scheduler is enabled by setting `SchedulerType=sched/backfill` in `slurm.conf`. Several `SchedulerParameters` can be used to tune its behavior, such as `bf_interval` (how often to run the backfill calculation), `bf_resolution` (time resolution of the simulation), `bf_window` (how far into the future to simulate), `bf_max_job_test` (maximum number of jobs to test for backfill), and `bf_max_job_user` (maximum jobs per user to test). Fine-tuning these parameters is often necessary to balance backfill effectiveness with scheduler overhead.

The selection of `sched/backfill` represents a fundamental choice to prioritize maximizing system utilization and job throughput, accepting the trade-offs of increased scheduler complexity and potentially less predictable job start orders from a user's perspective. This contrasts with `sched/builtin`'s focus on simplicity and strict priority adherence at the potential cost of efficiency.