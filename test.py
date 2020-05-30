import os
data_dir = os.path.join("..", "..", "Data", "cifar-10-batches-py",'test_batch')
data_dir = ".\\Data\\cifar-10-batches-py"
if os.path.exists(data_dir):
    print(data_dir+'  exist!')
else:
    print(data_dir+'  not exist')