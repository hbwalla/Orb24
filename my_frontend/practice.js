class Math {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    };

    add() {
        return this.x + this.y;
    };

    subtract() {
        return this.x - this.y;
    };

    multiply() {
        return this.x*this.y;
    };
};

var value = new Math(2,3);

console.log(value.multiply());