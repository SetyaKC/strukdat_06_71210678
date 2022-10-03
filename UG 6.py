class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def insert_head(self,new_rek,nama,saldo):
        new_rek = NodeTabungan(new_rek,nama,saldo)
        if self.isEmpty() == True:
            self._head = new_rek
            self.tail = new_rek
        else:
            new_rek.next = self._head
            self._head = new_rek
        self._size +=1

    def deleteHead(self):
        if self.isEmpty()== False:
            if self._size == 1:
                self._head = None
                self._tail = None
            else:
                hapus = self._head
                self._head = self._head._next
                hapus._next = None
                del hapus 
            self._size -=1 

    def deleteTail(self):
        if self.isEmpty()==False:
           if self._size == 1:
                self._head = None
                self._tail = None
        else:
            bantu = self._head
            while bantu._next != self._tail:
                bantu = bantu._next
            hapus = self._tail
            self._tail = bantu
            self._tail._next = None
            del hapus 
        self._size -=1 

    def delete(self,position):
        if self._size == 0:
            return False
        elif position == 0:
            self._deleteHead()
        elif position +1 >= self._size:
            self._deleteTail()
        else:
            delete_node = self._head
            for i in range(position):
                delete_node = delete_node._next

            bantu = self._head
            while bantu._next != delete_node:
                bantu = bantu._next
            bantu._next = delete_node._next
            del delete_node
            self._size -= 1

    # def filter(self,saldo):
    #     if self.isEmpty()==True:
    #         if self

    # def update(self,bunga):
    #     bantu = self._head
    #     while bantu! = None:
    #         print()

    def print(self):
        bantu = self._head
        while bantu!= None:
            # print(bantu._element)
            bantu = bantu.next
        print(f"Norek  : ,{bantu.no_rekening}")
        print(f"Nama   : ,{bantu.nama}")
        print(f"Saldo  : ,{bantu.saldo}")

slnc = SLNC()
slnc.insert_head(201,"Hanif",250000)
slnc.insert_head(110,"Yudha",150000)
slnc.print()
# slnc.filter(100)
slnc.print()
# slnc.update(200)
# slnc.update (50)
slnc.print()

