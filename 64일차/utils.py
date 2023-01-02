import numpy as np
import torch
import matplotlib.pyplot as plt


def train(num_epochs, train_loader, val_loader, model, optimizer, criterion,
          device, save_path):

    valid_loss_min = np.Inf
    train_loss_ls = []
    valid_loss_ls = []

    for epoch in range(1, num_epochs+1):
        train_loss = 0.0
        val_loss = 0.0
        train_loss_temp = 0.0
        val_loss_temp = 0.0
        train_batch = 0.0
        val_batch = 0.0

        # model train
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader):
            # move to gpu
            datas, targets = data.to(device), target.to(device)
            output = model(datas)

            loss = criterion(output, targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # update training loss
            train_loss_temp = train_loss_temp + ((1 / (batch_idx+1)) * (loss.data - train_loss_temp))
            train_loss += train_loss_temp.item()
            train_batch += 1

        # val model
        for batch_idx, (data, target) in enumerate(val_loader):
            # move to gpu
            datas, targets = data.to(device), target.to(device)
            output = model(datas)

            loss = criterion(output, targets)

            # update valid loss
            val_loss_temp = val_loss_temp + ((1 / (batch_idx+1)) * (loss.data - val_loss_temp))
            val_loss += val_loss_temp.item()
            val_batch += 1

        print('Epoch {} \t Training Loss: {:.6f} \t Validation Loss: {:.6f}'.format(
            epoch, train_loss, val_loss
        ))

        train_loss_ls.append(train_loss/train_batch)
        valid_loss_ls.append(val_loss/val_batch)

        if val_loss <= valid_loss_min:
            print("Validation loss decreased ({:.6f} --> {:.6f}). Saving Model...".format(
                valid_loss_min, val_loss
            ))
            torch.save(model.state_dict(), save_path)
            valid_loss_min = val_loss


    # loss 그래프 표현
    plt.plot(train_loss_ls, '-o')
    plt.plot(valid_loss_ls, '-o')
    plt.xlabel('Epoch')
    plt.ylabel("Loss")
    plt.legend(['train, val'])
    plt.title('Train vs Val Loss')
    plt.show()

