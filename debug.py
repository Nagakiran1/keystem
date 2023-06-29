from keystem import KeyStem

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal).
         A supervised learning algorithm analyzes the training data and produces an inferred function,
         which can be used for mapping new examples. An optimal scenario will allow for the
         algorithm to correctly determine the class labels for unseen instances. This requires
         the learning algorithm to generalize from the training data to unseen situations in a
         'reasonable' way (see inductive bias).
      """
doc = ['microsoft 365', 'manage subscription', '365 business', 'subscription admin', '365 admin', 'use microsoft', 'subscription payment', 'subscription', 'billing details', 'standard microsoft', 'steps microsoft', 'billing', 'business standard', 'com manage', 'signed microsoft', 'microsoft com', 'payment billing', 'admin microsoft', 'standard manage', 'excel powerpoint', 'onmicrosoft com', 'microsoft', 'powerpoint invite', 'word excel', 'install word', '365', 'excel', 'admin centre', 'powerpoint', 'com sign']

ks_model = KeyStem()
keywords = ks_model.get_keygroups(doc)
print(keywords)