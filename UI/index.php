<!DOCTYPE html>
<html>
    <head>
        <title>File Upload</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
        <script>
            var loadFile = function(event) {
                var image = document.getElementById('output');
                image.src = URL.createObjectURL(event.target.files[0]);
            };
        </script>
    </head>
    <body style="background-color: burlywood;">
        <center>
            <form action="upload.php" method="post" enctype="multipart/form-data">
                <table>
                    <th style="font-size:26px; font-family: sans-serif;">Select image to Upload and Predict:</th>
                    <tr></tr>
                    <tr>
                        <td><input type="file" name="fileToUpload" id="fileUploaded" onchange="loadFile(event)"></td>
                    </tr>
                    <tr></tr>
                    <tr>
                        <td><input type="submit" value="Upload File" name="submit">&nbsp;Click to Upload</td>
                    </tr>
                    </table>
                <img id="output" src="#" alt="Please Upload an Image" style="width: 100%;" />
            </form>
        </center>
    </body>
</html>