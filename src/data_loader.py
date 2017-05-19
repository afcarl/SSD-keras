from utils.XML_parser import XMLParser
from utils.COCO_parser import COCOParser

class DataLoader(object):
    """Class for loading VOC2007 and COCO datasets or
    """
    def __init__(self, dataset_name='VOC2007', dataset_path_prefix=None):

        self.dataset_name = dataset_name
        self.dataset_path_prefix = dataset_path_prefix
        self.ground_truth_data = None
        if self.dataset_path_prefix != None:
            self.dataset_path_prefix = dataset_path_prefix
        elif self.dataset_name == 'VOC2007':
            self.dataset_path_prefix = '../datasets/VOCdevkit/VOC2007/Annotations/'
            self.ground_truth_data = self._load_VOC2007()
        elif self.dataset_name == 'COCO':
            self.dataset_path_prefix = '../datasets/COCO/'
            self.ground_truth_data = self._load_COCO()
        elif self.dataset_name == 'all':
            raise NotImplementedError
        else:
            raise Exception('Incorrect dataset name:', self.dataset_name)

    def get_data(self):
        return self.ground_truth_data

    def _load_VOC2007(self):
        ground_truth_manager = XMLParser(self.dataset_path_prefix)
        return ground_truth_manager.get_data()

    def _load_COCO(self):
        ground_truth_manager = COCOParser(self.dataset_path_prefix)
        return ground_truth_manager.get_data()

