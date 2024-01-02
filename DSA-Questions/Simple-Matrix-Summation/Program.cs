// See https://aka.ms/new-console-template for more information

List<List<int>> TwoDimensionMatrix = new List<List<int>>();
TwoDimensionMatrix.Add(new List<int>() { 1, 2, 3 });
TwoDimensionMatrix.Add(new List<int>() { 4, 5, 6 });
SimpleMatrixSummation(TwoDimensionMatrix);


void SimpleMatrixSummation(List<List<int>> TwoDimensionMatrix)
{
    List<List<int>> ResultMatrix = new List<List<int>>();
    for (int i = 0; i <TwoDimensionMatrix.Count; i++)
    {
        List<int> tempmatrix = new();
        for (int j = 0; j <= TwoDimensionMatrix.Count; j++)
        {
            int newVal = GetSum(TwoDimensionMatrix, i, j);
            tempmatrix.Add(newVal);
        }
        ResultMatrix.Add(tempmatrix);
    }
    foreach (var matrix in ResultMatrix)
        Console.WriteLine(string.Join(" ", matrix));
    Console.ReadLine();
}
int GetSum(List<List<int>> TwoDimensionMatrix, int rowLimit, int columnLimit)
{
    int result = 0;
    for (int i = 0; i <= rowLimit; i++)
    {
        for (int j = 0; j <= columnLimit; j++)
        {
            result += TwoDimensionMatrix[i][j];
        }
    }
    return result;
}