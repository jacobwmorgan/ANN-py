using Dendrite;
namespace kms
{
    public class Neuron
    {
        public List<Dendrite> Dendrites { get; set; }
        public double Bias { get; set; }
        public double Delta { get; set; }
        public double Value { get; set; }

        public int DendriteCount 
        {
            get
            { 
                return Dendrites.Count;
            }
        }

        public Neuron(double _weights , double _bias)
        {
            this.Bias = _bias;
            this.Dendrites = new List<Dendrite>();
        }

    }
}