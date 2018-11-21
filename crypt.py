from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb9ZTm9fFagrzNRWJBgJNjxwnyvHAxtVZLfZvUrhehsRKFfIolRE7FrTKEMxuJug-gA_eCdrKpx4BAntIZnbYoBSXSRN_FUdTRfNW3icMqufoPzcaiQQr8ZiQ8FZgmrpGl5hbpvX-HjYxw_MIOdrHq_l7xdCLqqoiomNI0hUNG9OnYLi2A2y3pUTMC12_qTBdEiuyD'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
