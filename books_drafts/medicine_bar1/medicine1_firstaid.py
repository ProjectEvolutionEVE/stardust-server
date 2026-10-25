"""Medicine, bar 1: First Aid Principles. General principles only: no procedures, steps or doses."""
CODE = 'medicine1_firstaid'
BOOK = {
    "title": 'First Aid Principles',
    "subtitle": 'Stay calm, check for danger, call for help, and know your limits',
    "chapters": [
        ('Stay calm',
         'Panic makes everything harder. Take a breath, look around and think before you act. A calm person can notice danger, judge what is happening and get help.'),
        ('Check for danger first',
         'Before you go to anyone, make sure the area is safe for you too. A rescuer who is hurt cannot help anyone. Move away from fire, smoke, leaks or anything else that could cause more harm.'),
        ('Call for help',
         'Get help quickly. On Earth that means the local emergency number; aboard a ship, the crew in charge of medical care. Say clearly what happened, where it happened and how many people are hurt.'),
        ('Keep the person warm',
         'Cold can make an injured or unwell person worse. Cover them with a blanket or spare clothing, keep them comfortable and talk to them calmly while you wait for help.'),
        ('Do not move someone without need',
         'Moving an injured person can make the injury worse, especially to the neck or back. Move them only if they are in danger and cannot be kept safe where they are. Otherwise, leave the moving to trained people.'),
        ('Know your limits',
         'Good first aid means doing only what you have been trained to do. Learn the basics on a proper course, and keep a well-stocked first-aid kit where people can reach it. When in doubt, asking for trained help is always the right choice.'),
    ],
    "test": [
        ('What should you do first when someone is hurt?',
         [('a', 'Rush in at once'), ('b', 'Stay calm and check for danger'), ('c', 'Move them far away'), ('d', 'Give them food')], 'b'),
        ('Why must you check for danger before you help?',
         [('a', 'So you can leave early'), ('b', 'Because a hurt rescuer cannot help anyone'), ('c', 'To find the Market terminal'), ('d', 'Because danger always goes away')], 'b'),
        ('Who should you tell when you call for help aboard the Starship?',
         [('a', 'The Docking Bay'), ('b', 'Whoever is in charge of emergency care where you are'), ('c', 'The Market terminal'), ('d', 'The filing cabinet')], 'b'),
        ('Why keep an injured person warm?',
         [('a', 'Cold can make them worse'), ('b', 'Warm people never need help'), ('c', 'It makes the Starship go faster'), ('d', 'It stops all pain at once')], 'a'),
        ('When is it right to move an injured person?',
         [('a', 'Always, to be fair'), ('b', 'Whenever they ask you to'), ('c', 'Only when needed to keep them safe'), ('d', 'Never, in any case')], 'c'),
    ],
}
