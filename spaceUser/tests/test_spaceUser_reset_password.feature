Scenario: Reset a password of user
Given 'user' forgot the password 

When 'user ' performs an  'selected' 'mot de passe oublié''
Then 'system' performs an 'sends a form where to indicate recovery email' 

When 'user' performs an 'enter email in the form' 
And 'user' performs an 'validate the form'
Then 'system' performs an 'send an email with a password reset link'
And 'system' performs an 'displays a message that the email has been sent'

When 'user' performs an 'select reset link '
Then 'systeme' performs an 'displays a form to change the password'

When 'user' performs an 'enter the new password in the form'
And 'user' performs an 'validate the form'
Then 'system' performs an 'displays a validation message and a link to authenticate'







