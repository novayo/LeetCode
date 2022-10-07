

from cmath import log

global GLOBAL = {
    'conn': ctx
}

flask


@api.route("/hotfix", methods=['POST'])
@flask.timeout(3)
def do_hotfix():
    try:
        Lock
        寫log

        tran = create_transaction(GLOBAL['conn'])
        寫入獎池history
        寫入獎池
          tran.submit(...)
           if tran.create_time
              tran.rollback()
            else:
                create_time

        if end - start > 3:
            tran.rollback()
        else:
            tran.submit()  # cost time
    except Exception as ex:
        ...
    finally:
        release Lock
