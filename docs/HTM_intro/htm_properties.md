# Properties of HTM

## Sparse Distributed Representations

[Sparse distributed representations](https://numenta.com/assets/pdf/biological-and-machine-intelligence/BaMI-SDR.pdf) is a core data structure of HTM. A complete mathematical explanations is in this [paper](https://arxiv.org/pdf/1503.07469.pdf).

The reason why it is termed as Sparse is because of the fact that only few neurons fire when a cognitive task is performed i.e. if you take a snapshot of neurons in a brain, it is highly likely that you will only see less than ~2% neurons in an active state. An SDR consists of thousands of bits where at any point in time a small percentage of the bits are 1's and the rest are 0's. The bits in SDR corresponds to neurons in the brain, a 1 being a relatively active neuron and a 0 being a relatively inactive neuron.

```{figure} images/sdr.png
---
---
Sparse distributed representations.
```

## Encoding

The encoder converts the native format of the data into an SDR that can be fed into an HTM system. The encoder is responsible for determining which output bits should be ones, and which should be zeros, for a given input value in such a way as to capture the important semantic characteristics of the data. Similar input values should produce highly overlapping SDRs. This can be thought to be analogous with functions of the human sensory organs for instance converting frequencies and amplitudes of sounds into a set of Sparse distributed Representations. Certain properties that should be taken into note while encoding a sensory data are,

- Semantically similar data should result in SDRs with overlapping active bits.

- Same input should always produce the same SDR as an output.

- The output should have the same dimensionality for all the inputs.

- The output should have similar sparsity for all inputs and have enough one bits to deal with noise and subsampling.

## Spatial Pooling

Spatial pooling Algorithm is for solving problems to represent the input active neurons (comping from sensory or motor organs) to make that the cortex learn the pattern of sequences. It accepts the input vector of different sizes and represents it into sparse vectors of same size(It kind of normalises it). The output of the Spatial Pooler represents the mini columns i.e the pyramidal neuron in the cortices. It posses certain properties like maintaining a fixed sparsity i.e no matter how many bits are on and off in the input the spatial pooler need to maintain the fixed sparsity and to maintain the overlap properties i.e two similar inputs should produce similar outputs in the columns.


```{figure} images/spooling.png
---
---
Spatial pooling.
```

## Learning

Learning happens only in those columns of the Spatial Pooler which are active. All the connections that are falling in the input space, the permeance value will increase for them i,e the synaptic connection between them will strengthen while any connections that fall outside of the input space for those the permeance value will be decremented . Learning Spatial Pooler learns better in comparison to the Random Spatial Pooler. This step has been basically derived from the concept ‘Hebbian Learning: Neurons that fire together wire together ’.

For instance, in the diagram given below for any given column in a Spatial Pooler those cell that are connected to the active cells in the input space (i.e which are in green) their permeance will be incremented else those connected outside the input space their permeance will be decremented(the one’s in grey). No inactive column will learn anything.

```{figure} images/learning.png
---
---
Learning in spatial pooler.
```

## Boosting

In order for a column in a Spatial pooler to exist it should be a winning column i.e the overlap score should be above some threshold value while non-winning columns are inhibited from learning. Only the winner columns can update their permanence values. Boosting helps to change the overlap score before the inhibition occurs giving less active columns a better chance to express themselves and diminishing columns that seem overactive . Boosting on better enables the learning of input data i.e it improves the efficiency. In other words we can say that the columns that have low overlap score are boosted so that they can better express themselves and all the columns with higher overlap score are inhibited because they are expressing themselves too much.

## Temporal pooling

Temporal Pooling enables us to understand the sequential pattern over time. It learns the sequences of the active column from the Spatial Pooler and predicts what spatial pattern in coming next based on the temporal context of each input.

There are two primary steps of the Temporal Pooling algorithm. First, which cells within active columns will become active at a certain timestamp second, once the activation has been identified choose a set of cells to be in predictive state i.e those cells which will be firing on the next timestamp. Here , in this biological pyramidal neuron the proximal synapses lead directly to action potentials i.e they enable the learning of the sequence whereas patterns detected on the basal and apical dendrites depolarize the cell, representing predictions i.e cells that will fire at the next timestamp. Generally, at the first timestamp ‘Bursting’ occurs because their is no predictive state and after the first timestamp some cells become predictive which are all connected to the current firing cells. These cells will fire for the next timestamp.

Suppose, you are inputing the pattern ABCD and XBCY and you want the Temporal Memory to learn the sequence. After the input pattern has been converted to SDR and spatial columns activate the set of active neurons during the learning of sequence phase i.e TM phase when the columns sees the data for the first time, none of them are in predictive phase so ‘Bursting’ occurs meaning all the cells of the mini columns tries to learn that sequence and gets bursted . Once the column has learnt the sequence only a particular cell of the mini column gets activated and at the next time stamp those predictive cells gets activated.

```{figure} images/tpooling.png
---
---
Learning a sequence in temporal memory.
```

After the sequence is learned by the Temporal Memory upon inputting the A following sequence BC is predicted and upon inputting the sequence BC both D and Y is given as output as the temporal memory learns both the sequences ABCD and XBCY.

HTM has been implemented to industrial use and applied to various areas such as,

- HTM for Anomaly Detection.

- Rouge Behavior Detection

- Geospatial Tracking

- HTM for stocks

- Natural language Processing
