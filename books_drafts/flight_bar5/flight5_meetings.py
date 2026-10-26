"""Running Good Meetings: a clear purpose, an agenda, keeping to time, making decisions, taking notes, and following up after the meeting."""
CODE = "flight5_meetings"
BOOK = {
    "title": "Running Good Meetings",
    "subtitle": "A clear purpose, a short agenda, real decisions, and follow-up",
    "chapters": [
        ("Purpose",
         "Every meeting needs a clear purpose. If there is no reason to meet, the time is better spent on work. A simple sentence that says why the group is meeting helps everyone stay on track."),
        ("Agenda",
         "An agenda lists the topics in order and says what each one needs. Sending it before the meeting lets people prepare. A short agenda keeps the discussion focused."),
        ("Time",
         "Keep to the time you set. Give each topic a time limit and check the clock. A meeting that runs on past its end wastes the time of everyone present."),
        ("Decisions",
         "A good meeting ends with decisions, not only talk. Name the decision, who owns it and when it is due. Vague agreements are easy to forget."),
        ("Notes",
         "Write brief notes of what was decided and who will act. Notes give a shared record that everyone can check. Keep them short and clear."),
        ("Follow-up",
         "Follow up after the meeting to see whether actions were done. A quick check shows that the decisions matter. Without follow-up, meetings often repeat the same talk."),
    ],
    "test": [
        ("What should every meeting have?",
         [("a", "A loud sound system"), ("b", "No agenda"), ("c", "A clear purpose"), ("d", "No time limit")], "c"),
        ("What does an agenda do?",
         [("a", "Lists the topics in order and what each needs"), ("b", "Tells a joke"), ("c", "Records the weather"), ("d", "Cooks the meal")], "a"),
        ("What should a good meeting end with?",
         [("a", "Nothing decided"), ("b", "Decisions with an owner and a date"), ("c", "A song"), ("d", "A fight")], "b"),
        ("Why keep notes after a meeting?",
         [("a", "To hide the decisions"), ("b", "To use as a paper hat"), ("c", "To avoid work"), ("d", "To give a shared record of what was decided")], "d"),
        ("What does follow-up show?",
         [("a", "That meetings are pointless"), ("b", "That nobody needs to act"), ("c", "That the decisions matter"), ("d", "That the agenda is wrong")], "c"),
    ],
}
