## Sealed Secrets creation

```bash
kubectl create secret generic aws-secret \  --namespace sealed-secret \
  --from-file=creds="$HOME/.aws/credentials" \
  --dry-run=client -o yaml > secret.yaml
```

```bash
apiVersion: v1
kind: Secret
metadata:
  name: aws-secret
  namespace: sealed-secret
type: Opaque
data:
  aws_access_key_id: QUtJ...     # base64 encoded
  aws_secret_access_key: cVY2... # base64 encoded
```

```bash
kubeseal --controller-namespace sealed-secret --controller-name sealed-secret-sealed-secrets -o yaml < secret.yaml > aws-sealed-secret.yaml

```

