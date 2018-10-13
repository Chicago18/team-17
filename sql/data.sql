INSERT INTO users(username, fullname, location, email, company, affiliation, password, img_url)
VALUES
('jonny', 'Jonny Chow', 'Michigan', 'jonnny@umich.edu', 'JP Morgan', 'Straight', 'password', 'ben10.png');

INSERT INTO resources(name, body, person)
VALUES
("The Oxford English Dictionary Added 'Trans*.' Here's What the Label Means", "Precious Brady Davis says that she uses the label trans* to describe herself because it’s 'undefinable.' While that may be true in some senses, the experts at the Oxford English Dictionary have still given it their best shot.", 'KATY STEINMETZ', "2018/04/23"),
('An Equal Chance at Love: Why We Should Recognize Same-Sex Marriage', 'The debate about same-sex marriage often seems limited to two points of view. According to one, opposing the judicial invalidation of traditional marriage laws is tantamount to supporting segregationist racism.', 'JASON LEE STEORTS, "2018/02/10"'),
('Out & Equal at Work: From Closet to Corner Office', 'A major change is underway in today s workplace. Out & Equal at Work: From Closet to Corner Office is a groundbreaking anthology which chronicles personal narratives from straight allies and lesbian, gay, bisexual, and transgender (LGBT) executives and workplace leaders who have conquered adversity and ushered in policies that affirm and support the LGBT community in the workplace. ', 'Selisse Berry', "2018/02/22"),
('Allies at Work: Creating a Lesbian, Gay, Bisexual and Transgender Inclusive Work Environment', 'Dr. David M. Hall began his lesbian, gay, bisexual and transgender advocacy work while he was just a teenager. ', 'Dr. David M. Hall ', "2017/12/20");

INSERT INTO discussion(post, body, person)
VALUES
('Covering The Hidden Assault On Our Civil Rights', 'Against that conventional understanding, Kenji Yoshino argues that the demand to cover can pose a hidden threat to our civil rights. Though we have come to some consensus against penalizing people for differences based on race, sex, sexual orientation, religion, and disability, we still routinely deny equal treatment to people who refuse to downplay differences along these lines.', 'Kenji Yoshino'),
('Changing Corporate America from Inside Out: Lesbian and Gay Workplace Rights ', 'A long-overdue study, Nicole Raeburn’s analysis focuses on the mobilization of lesbian, gay, and bisexual employee networks over the past fifteen years to win domestic partner benefits in Fortune 1000 companies. ', 'Nicole Raeburn'),
('Lipstick or Golf Clubs: What Lesbian Leaders Understand About Success and What You Can Learn From Them', 'Being a lesbian is no longer a handicap in corporate and organizational America. It can be an asset, and a source of strength.', 'Julie Gedro'),
('EMPLOYERS RECOGNIZE IMPORTANCE OF LGBT BENEFITS TO ACCOMMODATE EVOLVING WORKFORCE, NEW MERCER SURVEY FINDS', 'The expansion of lesbian, gay, bisexual, and transgender (LGBT) rights and awareness has had profound impacts worldwide. As norms shift in society and the court of law, organizations are reassessing how they address LGBT-rights issues. ', 'Miriam Siscovick'),
('TALKING ABOUT RELIGIOUS EXEMPTIONS LAWS', 'Talking About Religious Exemptions Laws is a guide to building effective conversations about the ways in which harmful religious exemptions threaten not only laws that protect lesbian, gay, bisexual and transgender (LGBT) people from discrimination, but also health care (including women’s reproductive freedom), public safety, and more.', 'Howie');

INSERT INTO testimony(name, title, location, affiliation, company, email, img_url)
VALUES
('Dave Kim', 'FDlksjfalkjsdfjsdlfjsdaf', 'New York', 'Gay', 'JP', 'dave@gmail.com', 'pfp.png'),
('Jack The', 'FDlksjfalkjsdfjsdlfjsdaf', 'San Francisco', 'Gay', 'Sprite', 'jack@gmail.com', 'pfp.png'),
('June June', 'FDlksjfalkfsdjsdfjsdlfjsdaf', 'China', 'Lesbian', 'Coke', 'june@gmail.com', 'pfp.png'),
('May Thee', 'FDlksjfalkjsfdsadfjsdlfjsdaf', 'Russia', 'Transexual', 'Board', 'may@gmail.com', 'pfp.png'),
('Sprite Coke', 'FDlksjfalkjsfsadfjsdlfjsdaf', 'Portugal', 'Straight', 'Google', 'sprite@gmail.com', 'pfp.png');
