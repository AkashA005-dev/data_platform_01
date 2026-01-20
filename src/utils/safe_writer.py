import os
import shutil

def atomic_writer(temp_path , final_path):
    os.makedirs(os.path.dirname(final_path), exist_ok = True)

    if os.path.exists(final_path):
        os.remove(final_path)
    

    shutil.move(temp_path, final_path)