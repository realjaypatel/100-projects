import pandas as pd
import numpy as np
final_data = pd.read_csv("C:\\Users\\JaykumarPatel\\Downloads\\data.csv")
final_data['credit_amt'] = np.where(final_data['debit_amt']  < 0, final_data['credit_amt'].fillna(0) - final_data['debit_amt'],final_data['credit_amt'])
final_data['debit_amt'] = np.where(final_data['debit_amt'] < 0, 0, final_data['debit_amt'])
final_data['reconciliation_status'] = np.select(
   [
       (final_data['credit_amt'] != 19051) &(final_data['debit_amt']!=0) & ((final_data['credit_amt'] == 0) | (final_data['credit_amt'].isnull())),  # GL1 Credit only
       (final_data['foracid'] != 19051) &(final_data['debit_amt'] != final_data['credit_amt']) & (final_data['credit_amt'] != 0) & (final_data['debit_amt'] != 0) & ~final_data['credit_amt'].isnull() & ~final_data['debit_amt'].isnull(),               # Reversed for both GL1 and other GLs
       (final_data['foracid'] != 19051) &(final_data['credit_amt'] == final_data['debit_amt']) ,                 # Partial for both GL1 and other GLs
       (final_data['foracid'] == 19051) &(final_data['credit_amt'])!=0 & ((final_data['debit_amt'] == 0) |(final_data['debit_amt'].isnull())),  # GL1 Credit only
       (final_data['foracid'] == 19051) &(final_data['debit_amt'] != final_data['credit_amt']) & (final_data['credit_amt'] != 0) & (final_data['debit_amt'] != 0) & ~final_data['credit_amt'].isnull() & ~final_data['debit_amt'].isnull(),               # Reversed for both GL1 and other GLs
       (final_data['foracid'] == 19051) &(final_data['credit_amt'] == final_data['debit_amt']), 
    ],
   ['Not Reversed', 'Partially Reversed', 'Reversed','Not Reversed', 'Partially Reversed', 'Reversed'],
   default='Not Reversed'
)
print(final_data)


# data['status'] = np.where(data['reversal_amount'] ==0,'Not Reversed' ,
#                           np.where(data['financial_impact'] == data['reversal_amount'],'Reversed',data['status']))
