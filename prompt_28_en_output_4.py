<!DOCTYPE html>
<html>
<head>
    <title>Upload PDF</title>
</head>
<body>
    <form action="http://localhost:8000/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="pdf_file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>