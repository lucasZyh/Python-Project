class Phone:
    IMEI = None
    producer = None

    def call_by_4G(self):
        print("4G 通话")


class phone2(Phone):
    face_id = None

    def call_by_5G(self):
        print("5G 通话")


phone = phone2()
phone.call_by_4G()
phone.call_by_5G()
