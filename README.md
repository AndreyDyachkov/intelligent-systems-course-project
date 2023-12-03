# Intelligent systems course project
### Knowledge base
- Project_knowledge_base_v2 -- the knowledge base of the project (RDF)
- T4_project_cmap -- a concept map of the knowledge base (created in cmap)
- Project_knowledge_base_treeview -- a visualization of the processes in the knowledge base (Python, tkinter)
- Rules_v2 -- the rule base for the knowledge base (owl)
- Project_inconsistency_check_v2 -- a piece of code checking the knowledge base for inconsistency according to the rule base (Python)

### IPC
- server_side_v2 and client_side_v2 -- a simple IPC (inter-process communication) implementation via Sockets. An example of a client-server model where the client requests a threshold for the accuracy rate, written in the knowledge base, and the server responds to this request (Python, SPARQL) Run in different terminals.

### CNN
(code in kaggle: https://www.kaggle.com/code/andrewvd/lung-cancer-prediction-on-image-data)
- lung_cancer_recognition_on_image_data_train_model.ipynb - CNN
- lung-cancer-recognition_test_on_one_image.ipynb - test of the trained model (ct_scan_model1.h5) on 1 image
- ct_scan_model1.h5 -- a trained CNN model after oversampling with SMOTE
- ct_scan_model2.h5 -- a trained CNN with class-weighted approach
- ct_scan_model3.h5 -- a trained CNN after data augmentation
