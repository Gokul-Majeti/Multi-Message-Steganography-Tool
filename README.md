# 🕵️‍♂️ Multi-Message Steganography Tool

A Python-based GUI application that allows you to hide **multiple secret messages** inside a single image using the **Least Significant Bit (LSB)** steganography technique. The tool ensures secure and undetectable message embedding with easy encoding and decoding workflows.


## 📌 Features

- 🔐 Encode multiple secret messages in a single image.
- 🧠 Uses **LSB (Least Significant Bit)** technique for subtle and lossless data hiding.
- 🖼️ Supports only **PNG** format for accuracy and preservation of data.
- 🖥️ User-friendly **Tkinter GUI** interface.
- 🧩 Special character-based message separation for accurate decoding.
- 📂 All operations are handled through a simple, interactive window.


## 📸 Why Only PNG?

- **Lossless compression** ensures that hidden data is preserved.
- **JPEG or JPG** uses lossy compression and may **corrupt** embedded data.
- PNG offers **more capacity** and **visual integrity** for hidden data.


## 🔧 How It Works

### Encoding

1. Enter the number of messages to hide.
2. Select a PNG image.
3. Input each message one-by-one.
4. Messages are concatenated into a string with special separators: `@%` as a prefix and `#$` between each message.
5. The final string is encoded using **LSB technique** into the image.

### Decoding

1. Select the encoded PNG image.
2. LSB decoding extracts the hidden string.
3. If string starts with `@%`, the message is considered valid.
4. It splits the messages by `#$` and displays them.


## 🗂️ Project Structure

| File Name         | Description                                       |
|-------------------|---------------------------------------------------|
| `program.py`      | Main Python file to launch the GUI                |
| `background.png`  | Background image used in the GUI                  |


## 💻 Requirements

- Python 3.x
- Required Libraries:
  - Pillow (replacement for PIL)
  - tkinter
  - os

Install dependencies using:

pip install pillow
