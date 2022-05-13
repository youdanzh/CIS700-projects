# -*- coding: utf-8 -*-
"""Youdan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ffRGzazBTx8P-WA4DLgXNo9fZ04eEUJR
"""

'''Youdan's Approch'''

class Net(tr.nn.Module):
  def __init__(self, num_blocks, num_heads):
    super(Net, self).__init__()
    d_model = max_len+embeddings.shape[1]
    self.conv = tr.nn.Conv1d(max_len,max_len, kernel_size=1)    
    self.encoder = one_hot_positional_encoder(max_len)
    self.rrelu = tr.nn.LeakyReLU()
    self.blocks = tr.nn.ModuleList([
      MultiHeadAttention(num_heads, d_model, projections="QKVO")
      for _ in range(num_blocks)
    ])
    self.dense = tr.nn.Linear(embeddings.shape[1],embeddings.shape[0])
    self.readout =tr.nn.Linear(d_model, 2)
    
    
  def forward(self, example):
    x = embed(parse(example), max_len, embeddings)
    x = self.encoder(x)
   
    for mha in self.blocks:
      x = mha(x, x, x)
    x = self.conv(x)
    y = self.rrelu(self.readout(x)).mean(dim=0).unsqueeze(0)
    return y

net = Net(2, 4)
print(net(examples[0][0]))