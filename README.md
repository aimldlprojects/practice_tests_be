## Primary and Foreign Keys

| Table Name        | Primary Key         | Foreign Keys                                                              | Notes                                        |
| ----------------- | ------------------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| `users`         | `user_id`         | None                                                                      | -                                            |
| `subjects`      | `subject_id`      | None                                                                      | -                                            |
| `topics`        | `topic_id`        | `subject_id`→`subjects(subject_id)`                                  | Ensures topics are associated with subjects. |
| `questions`     | `question_id`     | `topic_id`→`topics(topic_id)`                                        | Ensures questions are tied to topics.        |
| `user_subjects` | `user_subject_id` | `user_id`→`users(user_id)`, `subject_id`→`subjects(subject_id)` | Manages user-subject relationships.          |
| `user_topics`   | `user_topic_id`   | `user_id`→`users(user_id)`, `topic_id`→`topics(topic_id)`       | Manages user-topic relationships.            |

## Relationships

#### User ↔ Subject (Many-to-Many)

* Managed through the `user_subjects` table.
* Secondary keys:
  * `user_id` in `user_subjects` references `users`.
  * `subject_id` in `user_subjects` references `subjects`.

#### User ↔ Topic (Many-to-Many)

* Managed through the `user_topics` table.
* Secondary keys:
  * `user_id` in `user_topics` references `users`.
  * `topic_id` in `user_topics` references `topics`.

#### Subject ↔ Topic (One-to-Many)

* Each subject can have multiple topics.
* Secondary key:
  * `subject_id` in `topics` references `subjects`.

#### Topic ↔ Question (One-to-Many)

* Each topic can have multiple questions.
* Secondary key:
  * `topic_id` in `questions` references `topics`.

## Expose project url to ngrok

* pyngrok
  * pip install pyngrok
  * pyngrok http http://127.0.0.1:8055
* ngrok
  * download ngrok.exe and place it in c:\ngrok directory.
  * add to environment variables > system path >c:\ngrok
  * ngrok http http://127.0.0.1:8055
