function what() {
    this.n = 1
    this.b = 2
}

a = what()
console.log(a)
b = new what()

console.log(new what())