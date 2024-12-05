from config import DB_PATH
import sqlite3


def add_post(title: str, content: str) -> None:
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        add_post_query,
        (
            title,
            content,
        ),
    )
    connection.commit()
    connection.close()

    # def get_posts():
    #     get_posts_query = """
    #     SELECT * FROM posts;
    #     """

    #     connection = sqlite3.connect(DB_PATH)
    #     cursor = connection.cursor()
    #     cursor.execute(get_posts_query)

    #     posts = cursor.fetchall()
    #     connection.close()

    # print(f"vot posty {posts}")


def delete_post(post_id: int) -> None:
    delete_post_query = """
    DELETE FROM posts WHERE post_id = ?
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        delete_post_query,
        (post_id,),
    )
    connection.commit()
    connection.close()

    print("ngl")


def get_post(post_id: int) -> None:
    get_post_query = """
    SELECT * FROM posts WHERE post_id = ?
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        get_post_query,
        (post_id,),
    )
    post = cursor.fetchone()
    connection.close()

    # post = cursor.fetchall()

    print(f"Vot post c id: {post_id}", post)


def update_post(post_id: int, new_title: str, new_content: str) -> None:
    update_post_query = """
    UPDATE posts SET title = ?, content = ? WHERE post_id = ?
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        update_post_query,
        (
            new_title,
            new_content,
            post_id,
        ),
    )
    updated_rows_count = cursor.rowcount

    connection.commit()
    connection.close()

    if updated_rows_count == 0:
        return "пост для обнавления не найден"
    else:
        return "пост обновлен"


print(update_post(2, "SQL2", "hachapurri"))

get_post(2)
# add_post("SQL", "hello worlds")
