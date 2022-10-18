/*

1. op버튼을 누르기 전까지 숫자를 계속 모은다

2. =이 아닌 다른 op버튼이 눌리면 이전까지 숫자를 하나로 뭉쳐서
    numArray에 저장하고 op버튼의 값을 opArray 저장한다

3. 1과 2를 반복하다가 =버튼을 누르면 다시 숫자 뭉치고
    그동안의 결과를 연산한다.

*/
let $num = $('.num')
let $op = $('.op')
let $screen = $('.screen')

let numbers = ''
let numArray = []
let opArray = []
let display = ''

function calculate() {
    let num1 = 0
    let num2 = 0
    let result = 0

    function numSet(num1) {
        num1 = parseInt(numArray[0])
        numArray.shift()
    }

    while (numArray.length > 1) {
        let opNow = opArray[0]
        opArray.shift
    
        if (opNow == '+') {
            numSet(num1)
            numSet(num2)

            numArray.unshift(num1 + num2)

        } else if (opNow == '-') {
            numSet(num1)
            numSet(num2)

            numArray.unshift(num1 - num2)

        } else if (opNow == '*') {
            numSet(num1)
            numSet(num2)

            numArray.unshift(num1 * num2)

        } else if (opNow == '/') {
            numSet(num1)
            numSet(num2)

            numArray.unshift(num1 / num2)

        } else if (numArray.length = 1) {
            numSet(result)
        }
    }
    return result
}

$num.on('click', function(e) {
    numbers += $(this).val()
    $screen.append($(this).val())
})

/*
1. 사칙연산일 때
    이전까지 숫자 뭉쳐서 array에 넣고 op도 array에 넣는다

2. = 일때
    배열 호출해서 계산한 다음, 그 값을 unshift해서 다시 넣는다.

3. c 일때
    초기화 한다
*/

$op.on('click', function(e) {
    if ((numbers !== '') && ($(this).val() !== '=')) {
        numArray.push(numbers)
        opArray.push($(this).val())
        $screen.append($(this).val())

    } else if ($(this).val() == '=') {
        $screen.append(calculate())

    } else if ($(this).val() == 'c') {
        numbers = ''
        numArray = []
        opArray = []
        $screen.empty()
    }

    $('.screen').text(display)
})