from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from core.quantum_unit import QuantumUnit
from utils.file_handler import FileHandler

router = APIRouter()
qu = QuantumUnit()
fh = FileHandler()

@router.post("/process/")
async def process_audio(background_tasks: BackgroundTasks, file: UploadFile = File(...), translate: bool = False):
    file_content = await file.read()
    saved_path = fh.save_upload(file_content, file.filename)
    
    result = qu.process_track(file.filename, translate=translate)
    
    return {"status": "success", "data": result}
