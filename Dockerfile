# ==========================================
# Stage 1: Build Binary
# ==========================================
FROM golang:1.23-alpine AS builder

# Install system dependencies (essential for compiling certain crypto/Go dependencies)
RUN apk add --no-cache git build-base ca-certificates

WORKDIR /app

# Cache Go modules layers to speed up subsequent builds
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the application source code
COPY . .

# Build the statically linked binary
# Note: If your project uses C-bindings (like secp256k1), change CGO_ENABLED to 1
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o frequency .

# ==========================================
# Stage 2: High-Performance Runtime
# ==========================================
FROM alpine:3.19 AS runner

# Ensure CA certificates and timezone data are present for secure RPC communication
RUN apk add --no-cache ca-certificates tzdata

WORKDIR /app

# Copy the compiled executable from the builder stage
COPY --from=builder /app/frequency .

# Optional: If your bot requires a configuration file or local environment assets, 
# uncomment the line below to bring them into the final image:
# COPY --from=builder /app/config.yaml ./config.yaml

# Set the binary as the container entrypoint
ENTRYPOINT ["./frequency"]
