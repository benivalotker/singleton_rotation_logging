# logging configuration
log_title = "logs"

win_log_path = "./logs/"

unix_log_path = "/opt/logs/"

file_name = "log.log"

log_format = "%(asctime)s - %(levelname)s - %(message)s"

log_level = 'DEBUG'         

file_size = 10*1024*1024    # 10 MB

file_num = 5