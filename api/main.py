from fastapi import FastAPI, HTTPException, Request, File, UploadFile
import uvicorn
from utilities.decryptor import decode_file
from utilities.encryptor import encode_file
import aiofiles
from utilities.compressor import compress_text

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Welcome to the Cryptify API"}

# api endpoint to accept a file and return the encrypted .ovl file


@app.post("/encrypt")
async def encrypt_file(file: UploadFile = File(...)):
    if file.filename.endswith(".ovl"):
        raise HTTPException(
            status_code=400, detail="File is already encrypted")
    # read and save file to data folder
    async with aiofiles.open(f"data/{file.filename}", "wb") as f:
        content = await file.read()
        await f.write(content)

    try:
        encoded_file_path = encode_file(f"data/{file.filename}")
        # return the contents of the encrypted file
        async with aiofiles.open(encoded_file_path, "rb") as f:
            # print file contents
            ciphertext = await f.read()
        return {"message": "File encrypted successfully", "ciphertext": compress_text(ciphertext)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# api endpoint to accept a file and return the decrypted file
@app.post("/decrypt")
async def decrypt_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".ovl"):
        raise HTTPException(
            status_code=400, detail="File is not a supported encrypted file")
    # read and save file to data folder
    async with aiofiles.open(f"data/{file.filename}", "wb") as f:
        content = await file.read()
        await f.write(content)

    try:
        decoded_file_path = decode_file(f"data/{file.filename}")
        # return the contents of the decrypted file
        async with aiofiles.open(decoded_file_path, "rb") as f:
            # print file contents
            plaintext = await f.read()
        return {"message": "File decrypted successfully", "plaintext": compress_text(plaintext)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
