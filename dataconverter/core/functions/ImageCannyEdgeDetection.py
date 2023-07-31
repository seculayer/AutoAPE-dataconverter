from typing import Any, List
from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants

class ImageCannyEdgeDetection(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT

    def apply(self, data:Any) -> list:
        _cv2 = CV2Utils.get_cv2()
        img = _cv2.cvtColor(data, _cv2.COLOR_BGR2RGB)
        canny_edge = _cv2.Canny(img, 100, 200)

        return [canny_edge]


if __name__ == '__main__':
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/iris.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)

    rst = ImageCannyEdgeDetection(stat_dict=None, arg_list=None).apply(img_data)
    print(rst[0])
    __cv2.imwrite(f"{image_path}/canny_rst.jpg", rst[0])
