import pandas as pd


def search_keyword(keyword):
    stock_list = pd.read_csv('./stock_list.csv', encoding='cp949')
    slist = stock_list['회사명']

    keyword_list = []

    for i in range(len(keyword)):
        keyword_list.append(keyword[i])

    # 노드 구조 생성
    class Node:
        def __init__(self, key, data=None):
            self.key = key
            self.data = []
            self.children = {}

    # 비어있는 헤드 노드 생성
    head = Node(None)

    # 회사명 리스트로 순회
    for target in slist:
        stock_name = target
        current_node = head

        # 회사명을 한 글자씩 순회하며 각 노드에 입력
        for spell in stock_name:
            if spell not in current_node.children:
                current_node.children[spell] = Node(spell)
                current_node.children[spell].data.append(stock_name)
            else:
                current_node.children[spell].data.append(stock_name)
            current_node = current_node.children[spell]

    b = keyword[0]
    a = head.children[b].data

    result = list()

    for i in a:
        if i.find(f'{keyword}') == 0:
            result.append(i)

    return result


if __name__ == '__main__':
    print(len(search_keyword('삼성')))
    print(search_keyword('삼성'))

