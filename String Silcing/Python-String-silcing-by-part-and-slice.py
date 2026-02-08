employee_info = "Ali Hamza|ID12345|2026-01-30|+92-300-1234567|developer_resume.pdf"
data_parts=employee_info.split('|')
print(type(data_parts))
user_name=data_parts[0]
print(user_name)
user_ID=data_parts[1]
