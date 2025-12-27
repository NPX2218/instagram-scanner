# Instagram Scanner

Find out who doesn't follow you back on Instagram. Available as both a web app and a Python script.

## 🌐 Web Version

**[Use it now](https://NPX2218.github.io/instagram-scanner/)**

No installation required. Just upload your files and get results instantly in your browser. All processing happens locally—your data never leaves your device.

## 🐍 Python Version

For those who prefer the command line.

### Setup

1. Clone this repo:

   ```bash
   git clone https://github.com/NPX2218/instagram-scanner.git
   cd instagram-scanner/python
   ```

2. Create a `files/` folder and add your Instagram data:

   ```bash
   mkdir files
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## 📥 Getting Your Instagram Data

1. Go to **Instagram → Settings → Account Center → Your information and permissions → Download your information**
2. Select **"Some of your information"** and choose only **"Followers and following"**
3. Choose **JSON** format
4. Download and extract the ZIP file
5. You'll need these two files:
   - `following.json`
   - `followers_1.json`

## 📁 Project Structure

```
instagram-scanner/
├── index.html          # Browser-based tool
├── python/
│   ├── main.py         # Command-line tool
│   └── files/          # Place your JSON files here (not tracked)
└── README.md
```

## License

This tool is **not affiliated with, endorsed, or associated with Instagram** in any way.

It is intended solely for **educational and personal use** with your own data export.

This tool must **not** be:

- Distributed to third parties
- Used for malicious purposes
- Used to abuse or interact with the Instagram API

## Author

By [Neel Bansal](https://github.com/neelbansal)
