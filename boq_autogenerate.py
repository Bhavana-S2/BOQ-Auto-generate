import pandas as pd
def generate_boq(input_file, output_file):
  try:
    df=pd.read_excel(input_file)
    boq=df.groupby(['category' , 'product'])['quantity'].sum().reset_index()
    boq.to_excel(output_file, index=False)
    print(f"Boq generated successfully and saved as {output_file}")
  except Exception as e:
    print("error:" , e)

generate_boq('input_template.xlsx", 'sample_output.xlsx')
      
