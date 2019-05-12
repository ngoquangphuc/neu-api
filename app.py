from flask import Flask
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

from data import NganhHoc, db
db.init_app(app)
app.app_context().push()
db.create_all()

class NganhHoc_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mo_ta', type=str, required=False, help='Mo ta co ban ve Nganh')
    parser.add_argument('khoa', type=str, required=False, help='Nganh thuoc Khoa')
    parser.add_argument('website', type=str, required=False, help='Website của Khoa')
    parser.add_argument('ma', type=str, required=False, help='Ma Nganh')
    parser.add_argument('chi_tieu', type=int, required=False, help='Chi tieu của Nganh')
    parser.add_argument('to_hop_xet_tuyen', type=str, required=False, help='To hop xet tuyen cua Nganh')
    parser.add_argument('diem_2015', type=str, required=False, help='Diem san 2015 cua Nganh')
    parser.add_argument('diem_2016', type=str, required=False, help='Diem san 2016 cua Nganh')
    parser.add_argument('diem_2017', type=str, required=False, help='Diem san 2017 cua Nganh')
    parser.add_argument('diem_2018', type=str, required=False, help='Diem san 2018 cua Nganh')
    parser.add_argument('chuong_trinh', type=str, required=False, help='Chuong trinh dao tao cua Nganh')
    parser.add_argument('so_tin', type=int, required=False, help='Tong so tin chi cua Nganh')
    parser.add_argument('co_hoi_nn', type=str, required=False, help='Co hoi nghe nghiep cua Nganh')
    
    
    
    def get(self, nganh):
        item = NganhHoc.find_by_name(nganh)
        if item:
            return item.json()
        return {'Message': 'Nganh hoc khong ton tai.'}
    
    def post(self, nganh):
        if NganhHoc.find_by_name(nganh):
            return {'Message': '{} da ton tai.'.format(nganh)}
        args = NganhHoc_List.parser.parse_args()
        item = NganhHoc(nganh, args['mo_ta'], args['khoa'], args['website'], args['ma'], args['chi_tieu'], args['to_hop_xet_tuyen'], args['diem_2015'], args['diem_2016'], args['diem_2017'], args['diem_2018'], args['chuong_trinh'], args['so_tin'], args['co_hoi_nn'])
        item.save_to()
        return item.json()
        
    def put(self, nganh):
        args = NganhHoc_List.parser.parse_args()
        item = NganhHoc.find_by_name(nganh)
        if item:
            item.mo_ta = args['mo_ta']
            item.khoa = args['khoa']
            item.website = args['website']
            item.ma = args['ma']
            item.chi_tieu = args['chi_tieu']
            item.to_hop_xet_tuyen = args['to_hop_xet_tuyen']
            item.diem_2015 = args['diem_2015']
            item.diem_2016 = args['diem_2016']
            item.diem_2017 = args['diem_2017']
            item.diem_2018 = args['diem_2018']
            item.chuong_trinh = args['chuong_trinh']
            item.so_tin = args['so_tin']
            item.co_hoi_nn = args['co_hoi_nn']
            item.save_to()
            return {'Nganh': item.json()}
        item = NganhHoc(nganh, args['mo_ta'], args['khoa'], args['website'], args['ma'], args['chi_tieu'], args['to_hop_xet_tuyen'], args['diem_2015'], args['diem_2016'], args['diem_2017'], args['diem_2018'], args['chuong_trinh'], args['so_tin'], args['co_hoi_nn'])
        item.save_to()
        return item.json()
            
    def delete(self, nganh):
        item  = NganhHoc.find_by_name(nganh)
        if item:
            item.delete_()
            return {'Message': '{} da duoc xoa.'.format(nganh)}
        return {'Message': '{} khong ton tai'.format(nganh)}
    
class All_NganhHoc(Resource):
    def get(self):
        return {'NganhHoc': list(map(lambda x: x.json(), NganhHoc.query.all()))}
    
api.add_resource(All_NganhHoc, '/')
api.add_resource(NganhHoc_List, '/<string:nganh>')

if __name__=='__main__':
    
    app.run(debug=True)