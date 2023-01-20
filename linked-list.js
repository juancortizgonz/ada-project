class LinkedList {
    constructor(element) {
        this.head = element;
        this.size = 1;
    }

    sizeOfList() {
        return this.size;
    }

    unionSet(linkedList) {
        let sizeFirstList = this.sizeOfList(),
            sizeSecondList = linkedList.sizeOfList();
    }
}