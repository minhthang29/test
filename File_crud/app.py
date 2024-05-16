import json
import boto3

def lambda_handler(event, context):
    # Tên bucket S3 mà bạn muốn tải file lên
    bucket_name = 'stephen-test-bucket1'
    
    # Tên file và đường dẫn tới file trên Lambda environment
    file_name = 'person1.txt'  # Thay đổi tên file nếu cần
    
    # Nội dung của file bạn muốn tải lên
    file_content = b'Hello, world!'
    
    # Khởi tạo S3 client
    s3 = boto3.client('s3')

    try:
        # Tải file lên S3
        response = s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        # Trả về kết quả
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File uploaded successfully!",
                "file_name": file_name,
                "bucket_name": bucket_name
            })
        }
    except Exception as e:
        # Xử lý lỗi nếu có
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "File upload failed",
                "error": str(e)
            })
        }
