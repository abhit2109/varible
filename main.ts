input.onButtonPressed(Button.A, function () {
    Counter = 1
})
input.onButtonPressed(Button.AB, function () {
    Counter = 0
})
input.onButtonPressed(Button.B, function () {
    Counter = -1
})
let Counter = 0
Counter = 0
basic.forever(function () {
    basic.showNumber(Counter)
})
