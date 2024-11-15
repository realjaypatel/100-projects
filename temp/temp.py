round(3.123,2)
numb = 100
# print(f"your scroll is {numb} and yeah that's good")
print(4/2)






final_data['reconciliation_status'] = np.select(
   [
       (final_data['debit_amt']) & ((final_data['credit_amt'] == 0) | (final_data['credit_amt'].isnull())),  # GL1 Credit only
       (final_data['debit_amt'] != final_data['credit_amt']) & (final_data['credit_amt'] > 0) & (final_data['debit_amt'] > 0),               # Reversed for both GL1 and other GLs
       (final_data['credit_amt'] == final_data['debit_amt']) ,                 # Partial for both GL1 and other GLs
       (final_data['gl_type'] == 'Cash Excess') &(final_data['credit_amt'] & ((final_data['debit_amt'] == 0) | (final_data['debit_amt'].isnull()))),  # GL1 Credit only
      (final_data['gl_type'] == 'Cash Excess') &(final_data['debit_amt'] != final_data['credit_amt']) & (final_data['credit_amt'] > 0) & (final_data['debit_amt'] > 0),               # Reversed for both GL1 and other GLs
       (final_data['gl_type'] == 'Cash Excess') &(final_data['credit_amt'] == final_data['debit_amt']), 
    ],
   ['Not Reversed', 'Partially Reversed', 'Reversed','Not Reversed', 'Partially Reversed', 'Reversed'],
   default='Unknown'
)
