# Mixtral

Mixtral is a [Mixture of Experts](../moe/MoE.md) model. Although it is a 4x7B model, it does not have 56B parameters but only 47B cause only the FFN layers are 8x, the rest of the parameters are shared by the experts.

Correlation of weights between mistral 7b and mixtral 8x7b. Did Mistral [upcycle](https://arxiv.org/abs/2212.05055) to get MoE from their dense model?