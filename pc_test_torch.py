from __future__ import print_function
import torch
from torch.autograd import Variable

### tensors
# x = torch.Tensor(5,3)
# x = torch.rand(5, 3)
# print(x)
# print(x.size())

# y = torch.rand(5, 3)
# print(y)

# y.add_(x)
# print(y)

# if torch.cuda.is_available():
#     x = x.cuda()
#     y = y.cuda()
#     x+y

### numpy bridge
# a = torch.ones(5)
# b = a.numpy()

# a.add_(1)

# print(a)
# print(b)

### autograd
x = Variable(torch.ones(2,2), requires_grad=True)
y = x+2
y.creator #? no creator attribute

z=y*y*3
out=z.mean()

x.grad