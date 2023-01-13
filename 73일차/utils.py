import os
from PIL import Image
import torch

IMG_FORMATS = ['.jpg', '.png', '.JPG', '.PNG']


def image_file_list(image_folder_path):
    # 폴더에서 파일 서치하는 함수

    all_root = []
    for (path, dir, files) in os.walk(image_folder_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext in IMG_FORMATS:
                root = os.path.join(path, filename)
                all_root.append(root)
            else:
                print('no image found...')
                continue

    return all_root


def expand2square(pil_image, background_color):
    width, height = pil_image.size
    if width == height:
        return pil_image
    elif width > height:
        result = Image.new(pil_image.mode, (width, width), background_color)
        result.paste(pil_image, (0, (width-height) // 2))
        return result
    else:
        result = Image.new(pil_image.mode, (height, height), background_color)
        result.paste(pil_image, ((height-width) // 2, 0))
        return result


def train(num_epoch, model, train_loader, val_loader, criterion,
          optimizer, save_dir, device):
    print('Start training......')
    running_loss = 0.0
    total = 0
    best_loss = 9999

    for epoch in range(num_epoch):
        for i, (imgs, labels) in enumerate(train_loader):
            imgs, labels = imgs.to(device), labels.to(device)

            output = model(imgs)
            loss = criterion(output, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            _, argmax = torch.max(output, 1)
            acc = (labels == argmax).float().mean()
            total += labels.size(0)

            if (i + 1) % 10 == 0:
                print('Epoch [{}/{}] Step [{}/{}] Loss: {:.4f}, Acc: {:.2f}%'.format(
                    epoch + 1, num_epoch, i+1, len(train_loader),
                    loss.item(), acc.item() * 100
                ))

        avrg_loss, val_acc = validation(model, val_loader, criterion, device)

        # if epoch % 10 == 0:
        #     save_model(model, save_dir, file_name=f'{epoch}.pt')

        if avrg_loss < best_loss:
            print(f'Best save at epoch >> {epoch}')
            print('Save model in ', save_dir)
            best_loss = avrg_loss
            save_model(model, save_dir)

    save_model(model, save_dir, file_name='last_resnet.pt')


def validation(model, val_loader, criterion, device):
    print('Start validation....')

    with torch.no_grad():
        model.eval()

        correct = 0
        total_loss = 0
        cnt = 0
        batch_loss = 0

        for i, (imgs, labels) in enumerate(val_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            output = model(imgs)
            loss = criterion(output, labels)
            batch_loss += loss.item()

            total_loss += imgs.size(0)
            _, argmax = torch.max(output, 1)
            correct += (labels == argmax).sum().item()
            total_loss += loss
            cnt += 1

    avrg_loss = total_loss / cnt
    val_acc = (correct / cnt * 100)
    print('val Acc: {:.2f}% avg_loss: {:.4f}'.format(
        val_acc, avrg_loss
    ))
    model.train()

    return avrg_loss, val_acc


def save_model(model, save_dir, file_name='best_vgg16.pt'):
    output_path = os.path.join(save_dir, file_name)

    torch.save(model.state_dict(), output_path)
