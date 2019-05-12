from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class NganhHoc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    mo_ta = db.Column(db.String(255), unique=False, nullable=False)
    khoa = db.Column(db.String(50), unique=False, nullable=False)
    website = db.Column(db.String(50), unique=False, nullable=False)
    ma = db.Column(db.String(10), unique=False, nullable=False)
    chi_tieu = db.Column(db.Integer, unique=False, nullable=False)
    to_hop_xet_tuyen = db.Column(db.String(30), unique=False, nullable=False)
    diem_2015 = db.Column(db.String(10), unique=False, nullable=False)
    diem_2016 = db.Column(db.String(10), unique=False, nullable=False)
    diem_2017 = db.Column(db.String(10), unique=False, nullable=False)
    diem_2018 = db.Column(db.String(10), unique=False, nullable=False)
    chuong_trinh = db.Column(db.String(255), unique=False, nullable=False)
    so_tin = db.Column(db.Integer, unique=False, nullable=False)
    co_hoi_nn = db.Column(db.String(255), unique=False, nullable=False)
    
    def __init__(self, name, mo_ta, khoa, website, ma, chi_tieu, to_hop_xet_tuyen, diem_2015, diem_2016, diem_2017, diem_2018, chuong_trinh, so_tin, co_hoi_nn):
        self.name = name
        self.mo_ta = mo_ta
        self.khoa = khoa
        self.website = website
        self.ma = ma
        self.chi_tieu = chi_tieu
        self.to_hop_xet_tuyen = to_hop_xet_tuyen
        self.diem_2015 = diem_2015
        self.diem_2016 = diem_2016
        self.diem_2017 = diem_2017
        self.diem_2018 = diem_2018
        self.chuong_trinh = chuong_trinh
        self.so_tin = so_tin
        self.co_hoi_nn = co_hoi_nn
        
    def json(self):
        return {'Name': self.name, 'Mo ta': self.mo_ta, 'Khoa': self.khoa, 'Website': self.website, 'Ma': self.ma, 'Chi tieu': self.chi_tieu, 'To hop xet tuyen': self.to_hop_xet_tuyen, 'Diem 2015': self.diem_2015, 'Diem 2016': self.diem_2016, 'Diem 2017': self.diem_2017, 'Diem 2018': self.diem_2018, 'Chuong trinh dao tao': self.chuong_trinh, 'Tong so tin chi': self.so_tin, 'Co hoi nghe nghiep': self.co_hoi_nn}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()
        
    
