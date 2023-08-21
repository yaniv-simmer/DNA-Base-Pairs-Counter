params.fasta_file_path = ''

process countPairs{
  input:
    path data_path
  output:
    stdout

  script:
  """
  python3 ../../../plot_histogram.py '${data_path}'
  """
}

workflow {
    if (params.fasta_file_path == '') {
    println  "\nError : No parameters were given"
  } else {
    seq_fasta_file = file(params.fasta_file_path)
    countPairs(seq_fasta_file) | view { it.trim() }
  }
}