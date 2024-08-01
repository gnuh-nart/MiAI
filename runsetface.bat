python src/setface.py
python src/align_dataset_mtcnn.py  src/Dataset/FaceData/raw src/Dataset/FaceData/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25
python src/classifier.py TRAIN src/Dataset/FaceData/processed Models/20180402-114759.pb src/Models/facemodel.pkl --batch_size 1000
