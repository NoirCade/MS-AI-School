import qrcode

# with open? - () 범위가 끝나면 파일을 자동으로 닫아줌!

with open('site_list.txt', 'rt', encoding='UTF8') as f:
  read_lines = f.readlines()

  for line in read_lines:
    line = line.strip()
    # *.strip? - 텍스트 이외의 요소들을 모두 제거해줌
    print(line)

    qr_data = line
    qr_image = qrcode.make(qr_data)

    qr_image.save(qr_data + '.png')