from django.core.management.base import BaseCommand
from apps.roadmap.models import Category, Phase, Topic, Project

class Command(BaseCommand):
    help = 'Populate the roadmap with AI and Quantum Computing learning paths'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing roadmap data...')
        Category.objects.all().delete()
        
        # Full-Stack AI Engineer Path
        ai_category = Category.objects.create(
            name='Full-Stack AI Engineer Path',
            code='AI',
            description='A comprehensive roadmap covering deep learning, MLOps, and large language models',
            order=1
        )
        self.stdout.write(f'Created category: {ai_category.name}')

        # AI Phases
        ai_phases = [
            {
                'title': 'Deep Learning Foundations',
                'week_range': 'Phase 1',
                'goal': 'Master fundamental deep learning concepts and PyTorch',
                'topics': [
                    'Neural network basics: perceptron, activation functions, forward/backprop',
                    'Loss functions (MSE, Cross-Entropy), optimizers (SGD, Adam)',
                    'Regularisation: dropout, batch norm, early stopping',
                    'CNNs: convolution, pooling, feature maps',
                    'RNNs/LSTMs/GRUs: sequence modeling',
                    'PyTorch: tensor operations, DataLoader, custom training loop'
                ],
                'projects': [
                    {
                        'name': 'Neural Network from Scratch',
                        'description': 'Implement a neural network from scratch using NumPy'
                    },
                    {
                        'name': 'CNN Image Classifier',
                        'description': 'Build and train a CNN for CIFAR-10 or MNIST classification'
                    },
                    {
                        'name': 'Deploy CNN with Streamlit',
                        'description': 'Create a web interface for your CNN classifier using Streamlit'
                    }
                ]
            },
            {
                'title': 'NLP & Transformers',
                'week_range': 'Phase 2',
                'goal': 'Master modern NLP techniques and transformer architectures',
                'topics': [
                    'Text preprocessing: tokenization, stemming, lemmatization',
                    'Word embeddings: Word2Vec, GloVe',
                    'Transformer architecture: self-attention, encoder/decoder',
                    'Fine-tuning pre-trained models: BERT, GPT, T5',
                    'NLP evaluation metrics: BLEU, ROUGE, perplexity'
                ],
                'projects': [
                    {
                        'name': 'Sentiment Analysis App',
                        'description': 'Fine-tune BERT for sentiment analysis with web interface'
                    },
                    {
                        'name': 'Text Summarizer',
                        'description': 'Implement text summarization using transformer models'
                    }
                ]
            },
            {
                'title': 'MLOps & Deployment',
                'week_range': 'Phase 3',
                'goal': 'Learn to deploy and maintain ML systems in production',
                'topics': [
                    'Serve models via API: FastAPI or Flask',
                    'Containerise with Docker',
                    'Experiment tracking / model versioning: MLflow, DVC',
                    'Pipeline orchestration: Airflow / Prefect',
                    'CI/CD basics: GitHub Actions / Jenkins',
                    'Cloud deployment: AWS EC2 / GCP VM / serverless',
                    'Monitoring & drift detection: logs, alerts'
                ],
                'projects': [
                    {
                        'name': 'Model API Deployment',
                        'description': 'Deploy fine-tuned NLP model as REST API'
                    },
                    {
                        'name': 'MLOps Pipeline',
                        'description': 'Create pipeline: training → evaluation → deployment'
                    },
                    {
                        'name': 'Cloud Model API',
                        'description': 'Deploy model to cloud with endpoint + documentation'
                    }
                ]
            },
            {
                'title': 'LLM & RAG Systems',
                'week_range': 'Phase 4',
                'goal': 'Build advanced AI systems with LLMs and retrieval',
                'topics': [
                    'LLM architecture fundamentals',
                    'Prompt engineering: zero-shot, few-shot, chain-of-thought',
                    'Retrieval-Augmented Generation (RAG) pipelines',
                    'Vector databases: FAISS, Chroma, Pinecone',
                    'Agent frameworks: LangChain, LlamaIndex'
                ],
                'projects': [
                    {
                        'name': 'RAG Chatbot',
                        'description': 'Build RAG chatbot for custom PDFs/data'
                    },
                    {
                        'name': 'Multi-agent Assistant',
                        'description': 'Create AI assistant with retriever + summarizer + agent'
                    },
                    {
                        'name': 'SQL AI Analyst',
                        'description': 'Develop chatbot that can query SQL database'
                    }
                ]
            },
            {
                'title': 'Scalable AI Systems & Advanced Topics',
                'week_range': 'Phase 5',
                'goal': 'Design and build production-ready AI systems',
                'topics': [
                    'Distributed training: PyTorch Lightning, Ray',
                    'Model compression/optimisation: ONNX export, quantization, pruning',
                    'Streaming pipelines: Kafka, Redis streams',
                    'Generative models: GANs, VAEs, diffusion models',
                    'Responsible AI: fairness, interpretability, model cards'
                ],
                'projects': [
                    {
                        'name': 'End-to-End AI Assistant',
                        'description': 'Build complete system with RAG + deployment + monitoring + CI/CD'
                    },
                    {
                        'name': 'Generative AI Demo',
                        'description': 'Create GAN image generator with web UI'
                    }
                ]
            },
            {
                'title': 'Portfolio & Career Prep',
                'week_range': 'Phase 6',
                'goal': 'Prepare portfolio and interview materials',
                'topics': [
                    'Clean up all GitHub repos (structured folder, README, screenshots)',
                    'Pin "AI Projects" on GitHub profile',
                    'Write LinkedIn posts about projects',
                    'Core ML/DL/MLOps interview concepts',
                    'System design (AI system architecture) preparation'
                ],
                'projects': [
                    {
                        'name': 'AI Portfolio README',
                        'description': 'Create comprehensive portfolio documentation with project links'
                    }
                ]
            }
        ]

        # Create AI phases
        for i, phase_data in enumerate(ai_phases, 1):
            phase = Phase.objects.create(
                category=ai_category,
                title=phase_data['title'],
                week_range=phase_data['week_range'],
                goal=phase_data['goal'],
                order=i
            )
            self.stdout.write(f'Created phase: {phase.title}')

            # Create topics
            for j, topic_name in enumerate(phase_data['topics'], 1):
                Topic.objects.create(
                    phase=phase,
                    name=topic_name,
                    order=j
                )
            
            # Create projects
            for j, project_data in enumerate(phase_data['projects'], 1):
                Project.objects.create(
                    phase=phase,
                    name=project_data['name'],
                    description=project_data['description'],
                    order=j
                )

        # Quantum Computing Path
        qc_category = Category.objects.create(
            name='Quantum Computing Extension',
            code='QC',
            description='Advanced extension covering quantum computing and quantum machine learning',
            order=2
        )
        self.stdout.write(f'Created category: {qc_category.name}')

        # Quantum Computing Phases
        qc_phases = [
            {
                'title': 'Quantum Foundations',
                'week_range': 'Phase 7',
                'goal': 'Master the fundamentals of quantum computing',
                'topics': [
                    'Qubits, superposition, entanglement basics',
                    'Dirac (bra-ket) notation',
                    'Quantum gates: Hadamard, S, T, X, Y, Z, CNOT',
                    'Linear algebra for quantum: matrices, eigenvalues/vectors, tensor products',
                    'Quantum circuits & simulation frameworks (basic)'
                ],
                'projects': [
                    {
                        'name': 'Quantum Circuit Simulator',
                        'description': 'Simulate simple quantum circuits (e.g., Bell state, simple gate sequences)'
                    }
                ]
            },
            {
                'title': 'Quantum Algorithms & ML Basics',
                'week_range': 'Phase 8',
                'goal': 'Understand core quantum algorithms and their ML applications',
                'topics': [
                    'Quantum algorithm overview (Grover, VQE, etc)',
                    'Hybrid quantum-classical algorithms (variational circuits)',
                    'Quantum kernel methods, quantum SVMs'
                ],
                'projects': [
                    {
                        'name': 'Quantum Classifier',
                        'description': 'Build a quantum-kernel classification demo (on simulator)'
                    }
                ]
            },
            {
                'title': 'Quantum ML & Hybrid Systems',
                'week_range': 'Phase 9',
                'goal': 'Build hybrid quantum-classical ML systems',
                'topics': [
                    'Hybrid quantum-classical ML: combining quantum circuits with classical layers',
                    'Use quantum ML libraries: PennyLane, TensorFlow Quantum',
                    'Map a classical ML problem into a quantum-enabled formulation'
                ],
                'projects': [
                    {
                        'name': 'Quantum-ML Pipeline',
                        'description': 'Create pipeline with quantum state embeddings and classification'
                    }
                ]
            },
            {
                'title': 'Advanced Quantum AI',
                'week_range': 'Phase 10',
                'goal': 'Explore cutting-edge quantum AI research',
                'topics': [
                    'Quantum error correction, scalability of quantum computers',
                    'Ethical/Responsible quantum AI',
                    'Current research directions and limitations'
                ],
                'projects': [
                    {
                        'name': 'Research Demo',
                        'description': 'Apply quantum ML algorithm to real dataset with analysis of limitations'
                    }
                ]
            }
        ]

        # Create Quantum Computing phases
        for i, phase_data in enumerate(qc_phases, 1):
            phase = Phase.objects.create(
                category=qc_category,
                title=phase_data['title'],
                week_range=phase_data['week_range'],
                goal=phase_data['goal'],
                order=i
            )
            self.stdout.write(f'Created phase: {phase.title}')

            # Create topics
            for j, topic_name in enumerate(phase_data['topics'], 1):
                Topic.objects.create(
                    phase=phase,
                    name=topic_name,
                    order=j
                )
            
            # Create projects
            for j, project_data in enumerate(phase_data['projects'], 1):
                Project.objects.create(
                    phase=phase,
                    name=project_data['name'],
                    description=project_data['description'],
                    order=j
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated roadmap data'))