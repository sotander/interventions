from connector import DB
from dbget import get_labeled_dialogues_ts01


def main():
    conn = DB()

    get_labeled_dialogues_ts01(conn, is_en=True, ts=1)

    conn.close_connection()


if __name__ == "__main__":
    main()
