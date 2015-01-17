from rauth.service import OAuth2Service

facebook = OAuth2Service(
    client_id='1555615041351747',
    client_secret='658848867b28074a4ebf22b9f374d724',
    name='facebook',
    authorize_url='https://graph.facebook.com/oauth/authorize',
    access_token_url='https://graph.facebook.com/oauth/access_token',
    base_url='https://graph.facebook.com/')