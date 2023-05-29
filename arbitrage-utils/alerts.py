

def alert_by_rules(data, alert, rules):
    """
    :param data: [
        {
            'exchange': 'ston.fi',
            'data': [
                {
                    'pair': 'TON/USDT',
                    'ask': 2,
                    'bid': 1,
                    'orderbook': {
                        'asks': [price, volume,), ...],
                        'bids': [(price, volume,), ...],
                    },
                },

            ],
        },

        {...}, ...
    ]
    :param alert: {
        'high_alert': function,
        'low_alert': function,
    }
    :param rules: {
        'default': {
            'high_alert': (0.05, 80,), # (percent spread, volume,)
            'low_alert': (0.05, 80,), # (percent spread, volume,)
        },
        'custom': [
            {
                'exchange': 'ston.fi',
                'ask': {
                    'high_alert': (0.05, 80,), # (percent spread, volume,)
                    'low_alert': (0.04, 80,), # (percent spread, volume,)
                },
                'bid': {
                    'high_alert': (0.05, 80,), # (percent spread, volume,)
                    'low_alert': (0.04, 80,), # (percent spread, volume,)
                }
            },
            {...}, ...
        ],
    }

    Description:
    -----------


    -----------
    :return:
    """
    pass